<?php
$host = "localhost";
$user = "";
$pass = "";
$db = "";

// Connessione al DB
$conn = new mysqli($host, $user, $pass, $db);
if ($conn->connect_error) die("Connessione fallita: " . $conn->connect_error);

// INSERIMENTO
if (isset($_POST['inserisci'])) {
    $intent = $_POST['intent'];
    $pattern = $_POST['pattern'];
    $response = $_POST['response'];

    $sql = "INSERT INTO intents (intent, pattern, response) VALUES (?, ?, ?)";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("sss", $intent, $pattern, $response);
    $stmt->execute();
}

// CANCELLAZIONE
if (isset($_POST['cancella']) && isset($_POST['selezionato'])) {
    $id = $_POST['selezionato'];
    $conn->query("DELETE FROM intents WHERE id = $id");
}

// MODIFICA
if (isset($_POST['modifica']) && isset($_POST['id_intent'])) {
    $id = $_POST['id_intent'];
    $intent = $_POST['intent'];
    $pattern = $_POST['pattern'];
    $response = $_POST['response'];

    $sql = "UPDATE intents SET intent=?, pattern=?, response=? WHERE id=?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("sssi", $intent, $pattern, $response, $id);
    $stmt->execute();
}

// DATI PER RIEMPIMENTO FORM IN CASO DI UPDATE
$update_data = ["", "", ""];
$id_intent = "";
if (isset($_POST['seleziona']) && isset($_POST['selezionato'])) {
    $id_intent = $_POST['selezionato'];
    $res = $conn->query("SELECT * FROM intents WHERE id = $id_intent");
    $row = $res->fetch_assoc();
    $update_data = [$row['intent'], $row['pattern'], $row['response']];
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Addestramento</title>
</head>
<body>
<h2>Addestramento chat bot AI</h2>

<form method="post">
    <input type="hidden" name="id_intent" value="<?= htmlspecialchars($id_intent) ?>">

    <label>Intent:</label><br>
    <input type="text" name="intent" value="<?= htmlspecialchars($update_data[0]) ?>"><br><br>

    <label>Pattern:</label><br>
    <input type="text" name="pattern" value="<?= htmlspecialchars($update_data[1]) ?>"><br><br>

    <label>Risposta:</label><br>
    <textarea name="response" rows="4" cols="50"><?= htmlspecialchars($update_data[2]) ?></textarea><br><br>

    <input type="submit" name="inserisci" value="Inserisci">
    <input type="submit" name="modifica" value="Modifica">
</form>

<h3>Lista Intents</h3>
<form method="post">
    <table border="1" cellpadding="5">
        <tr>
            <th>Seleziona</th>
            <th>ID</th>
            <th>Intent</th>
            <th>Pattern</th>
            <th>Risposta</th>
        </tr>

        <?php
        $res = $conn->query("SELECT * FROM intents ORDER BY id ASC");
        while ($row = $res->fetch_assoc()) {
            echo "<tr>";
            echo "<td><input type='radio' name='selezionato' value='{$row['id']}'></td>";
            echo "<td>{$row['id']}</td>";
            echo "<td>{$row['intent']}</td>";
            echo "<td>{$row['pattern']}</td>";
            echo "<td>{$row['response']}</td>";
            echo "</tr>";
        }
        ?>
    </table><br>

    <input type="submit" name="seleziona" value="Seleziona per Modifica">
    <input type="submit" name="cancella" value="Elimina">
</form>
</body>
</html>
