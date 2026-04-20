import tensorflow as tf
from tensorflow.keras import layers
import numpy as np

# --- 1. IL GENERATORE (Il Falsario) ---
def build_generator():
    model = tf.keras.Sequential([
        # Prende un vettore di 100 numeri casuali
        layers.Dense(7*7*256, input_shape=(100,)),
        layers.BatchNormalization(),
        layers.LeakyReLU(),
        layers.Reshape((7, 7, 256)),
        # Ingrandisce l'immagine fino a 28x28
        layers.Conv2DTranspose(128, (5, 5), strides=(1, 1), padding='same', use_bias=False),
        layers.BatchNormalization(),
        layers.LeakyReLU(),
        layers.Conv2DTranspose(64, (5, 5), strides=(2, 2), padding='same', use_bias=False),
        layers.BatchNormalization(),
        layers.LeakyReLU(),
        layers.Conv2DTranspose(1, (5, 5), strides=(2, 2), padding='same', use_bias=False, activation='tanh')
    ], name="Generator")
    return model

# --- 2. IL DISCRIMINATORE (Il Giudice) ---
def build_discriminator():
    model = tf.keras.Sequential([
        layers.Conv2D(64, (5, 5), strides=(2, 2), padding='same', input_shape=[28, 28, 1]),
        layers.LeakyReLU(),
        layers.Dropout(0.3),
        layers.Conv2D(128, (5, 5), strides=(2, 2), padding='same'),
        layers.LeakyReLU(),
        layers.Dropout(0.3),
        layers.Flatten(),
        layers.Dense(1) # Ritorna un punteggio: alto = vero, basso = falso
    ], name="Discriminator")
    return model

# Istanziamo i modelli
generator = build_generator()
discriminator = build_discriminator()

# --- 3. LOGICA DI PERDITA E OTTIMIZZAZIONE ---
cross_entropy = tf.keras.losses.BinaryCrossentropy(from_logits=True)

def discriminator_loss(real_output, fake_output):
    real_loss = cross_entropy(tf.ones_like(real_output), real_output)
    fake_loss = cross_entropy(tf.zeros_like(fake_output), fake_output)
    return real_loss + fake_loss

def generator_loss(fake_output):
    # Il generatore vuole che il discriminatore dia "1" (Vero) alle sue immagini finte
    return cross_entropy(tf.ones_like(fake_output), fake_output)

generator_optimizer = tf.keras.optimizers.Adam(1e-4)
discriminator_optimizer = tf.keras.optimizers.Adam(1e-4)

# --- 4. IL CICLO DI ADDESTRAMENTO (Training Step) ---
@tf.function
def train_step(images):
    noise = tf.random.normal([BATCH_SIZE, 100])

    with tf.GradientTape() as gen_tape, tf.GradientTape() as disc_tape:
        generated_images = generator(noise, training=True)

        real_output = discriminator(images, training=True)
        fake_output = discriminator(generated_images, training=True)

        gen_loss = generator_loss(fake_output)
        disc_loss = discriminator_loss(real_output, fake_output)

    # Calcolo e applicazione dei gradienti (aggiornamento pesi)
    gradients_of_generator = gen_tape.gradient(gen_loss, generator.trainable_variables)
    gradients_of_discriminator = disc_tape.gradient(disc_loss, discriminator.trainable_variables)

    generator_optimizer.apply_gradients(zip(gradients_of_generator, generator.trainable_variables))
    discriminator_optimizer.apply_gradients(zip(gradients_of_discriminator, discriminator.trainable_variables))

# --- 5. ESECUZIONE ---
BATCH_SIZE = 256

# Esempio di utilizzo con dati casuali (da sostituire con il tuo dataset reale)
# data = tf.random.normal([1000, 28, 28, 1]) 
# train_dataset = tf.data.Dataset.from_tensor_slices(data).shuffle(1000).batch(BATCH_SIZE)

print("Modelli pronti.")
generator.summary()
discriminator.summary()
