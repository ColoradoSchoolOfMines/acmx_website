<?php 
$this->load->database();
$query = $this->db->get('projects');
?>

<div class="row-fluid" id="projectmain">
<?= $row->name; ?>
<br />
<?= $row->information; ?>
</div>
<div class="row-fluid" id="projectinfo">
	<div class="span8" id="projectblog">
	left
	</div>
	<div class="span4" id="projectmembers">
	right
	</div>
</div>