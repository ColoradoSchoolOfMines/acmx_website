hello

<?php

$this->load->database();
$query = $this->db->get('acmxtest_table');
foreach ($query->result() as $row)
{
	echo "name: ".$row->name."<br>";
	echo "data: ".$row->anotherfield."<br><br>";
}

?>
