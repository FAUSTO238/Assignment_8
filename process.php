<?php
if (isset($_POST['mac_address']) && isset($_POST['dhcp_version'])) {
    // Receive the form data
    $mac_address = escapeshellarg($_POST['mac_address']);
    $dhcp_version = escapeshellarg($_POST['dhcp_version']);
    
    // Call the Python script to assign the IP address
    $command = escapeshellcmd("python3 /var/www/html/network_config.py $mac_address $dhcp_version");
    $output = shell_exec($command);
    
    // Display the result
    echo "<pre>$output</pre>";
} else {
    echo "Please provide both MAC address and DHCP version.";
}
?>
