<?php
$this->load->database();
$query = $this->db->get('projects');
foreach($query->result() as $row){
	if($project == $row->url){
		$name = $row->name;
		$id = $row->id;
		$info = $row->information;
	}
}
?>
<div class="row-fluid" id="projectmain">
<?= $name ?>
<br />
<?= $info ?>
</div>
<div class="row-fluid" id="projectinfo">
	<div class="span8" id="projectblog">
	left
	</div>
	<div class="span4" id="projectmembers">
	right
	</div>
</div>