<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>IP Address Request</title>
</head>
<body>
    <h1>Request IP Address</h1>
    <form action="process.php" method="post">
        <label for="mac_address">MAC Address:</label><br>
        <input type="text" id="mac_address" name="mac_address" required><br><br>

        <label for="dhcp_version">DHCP Version:</label><br>
        <select id="dhcp_version" name="dhcp_version" required>
            <option value="DHCPv4">DHCPv4</option>
            <option value="DHCPv6">DHCPv6</option>
        </select><br><br>

        <input type="submit" value="Request IP">
    </form>
</body>
</html>
