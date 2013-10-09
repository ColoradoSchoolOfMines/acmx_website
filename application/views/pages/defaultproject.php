<?php 
$this->load->database();
$query = $this->db->get('users');
foreach($query->result() as $row){
	echo $row->email;	
}
?>

<div class="row-fluid" id="projectmain">

</div>
<div class="row-fluid" id="projectinfo">
	<div class="span8" id="projectblog">
	left
	</div>
	<div class="span4" id="projectmembers">
	right
	</div>
</div>