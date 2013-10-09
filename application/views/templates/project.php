<?php
// Connect to the database and pre-load all the variables we'll need to output.
$this->load->database();
$query = $this->db->get('projects');
foreach($query->result() as $row){
	// We're collecting the entire project table's information and sorting through it with PHP, this is actually faster than sorting in MySQL.
	if($project == $row->url){
		// We only care about collecting the values for the project the user requested, naturally.  The $project variable came to use from the pages.php controller, it was passed to this script as $data['project'].
		$name = $row->name;
		$id = $row->id;
		$info = $row->information;
	}
}
// After this next "<?" delimiter we'll be outputting straight HTML.
?>
<div class="row-fluid" id="projectmain">
<?= $name // This is a quick-echo, a small snippet of PHP we're using to output this variable. ?>
<br />
<?= $info ?>
</div>
<div class="row-fluid" id="projectinfo">
	<div class="span8" id="projectblog">
		Blog element goes here
	</div>
	<div class="span4" id="projectmembers">
		Project members go here
	</div>
</div>
