<?php

class Pages extends CI_Controller {
	public function view($page = 'home')
	{
		// If the page requested isn't a "file," e.g. about or support, this will be true.
		if(!file_exists('application/views/pages/'.$page.'.php'))
		{
			// Chances are, they're looking for a project.  Connect to the database here.
			$this->load->database('acmx');
			$query = $this->db->get('projects');	// Pull the projects table.
			$names = [];	// Create an array for project names.
			foreach($query->result_array() as $row){	// Loop through the list of projects.
				$names[] = $row['url'];		// Get the smalltext version of the project name here
			}
			if(in_array($page, $names)){	// If the requested page is in the list of project names (that is, the project exists), continue.
				$data['project'] = $page;	// Send the requested page name to the project.php template, we'll grab all the required data from the DB there.
				$this->load->view('templates/header',$data);	// Output the header template
				$this->load->view('templates/project',$data);	// Output what the project.php template will produce given the $data array.
				$this->load->view('templates/footer',$data);	// Output the footer template
			}else{
				show_404();	// If this is running, then the file doesn't exist and we can't find any project by that name, we need the 404 page.
			}
		}else{
			// If this is running, a file by the name $page exists (this logic could be considered backwards but I don't really care)
			$data['title'] = ucfirst($page);	// Capitalize the first letter of the page name
			$this->load->view('templates/header', $data);	// Output the header template
			$this->load->view('pages/'.$page, $data);	// Output whatever the page by the name $page has to offer
			$this->load->view('templates/footer', $data);	// Output the footer template
		}
	}
}

?>