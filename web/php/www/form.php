<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
        <form action="string.php" method="get">
            Name: <input type="text" name="username">
            <br>
            Age: <input type="number" name="age">
            <input type="submit">
        </form>
        <br>
        My name is <?php echo $_GET["username"] ?> 
        <br>
        My Age is <?php echo $_GET["age"] ?>
</body>
</html>