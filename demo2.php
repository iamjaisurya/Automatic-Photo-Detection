<?php
system("rm -rf /var/www/html/uploads_sig/*");
$target_dir = "/var/www/html/uploads_sig/";
$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
$uploadOk = 1;
$imageFileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));

// Check if image file is a actual image or fake image
if(isset($_POST["submit"])) {
  $check = getimagesize($_FILES["fileToUpload"]["tmp_name"]);
  if($check !== false) {
    echo "File is an image - " . $check["mime"] . ".";
    $uploadOk = 1;
  } else {
    echo "File is not an image.";
    $uploadOk = 0;
  }
}

// Check if file already exists
if (file_exists($target_file)) {
  echo "Sorry, file already exists.";
  $uploadOk = 0;
}

// Check file size
if ($_FILES["fileToUpload"]["size"] > 500000) {
  echo "Sorry, your file is too large.";
  $uploadOk = 0;
}

// Allow certain file formats
if($imageFileType != "jpg" && $imageFileType != "png" && $imageFileType != "jpeg"
&& $imageFileType != "gif" ) {
  echo "Sorry, only JPG, JPEG, PNG & GIF files are allowed.";
  $uploadOk = 0;
}

// Check if $uploadOk is set to 0 by an error
if ($uploadOk == 0) {
  echo "Sorry, your file was not uploaded.";
// if everything is ok, try to upload file
} else {
  if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) {
    $code = "python3 sigchecker.py /var/www/html/uploads_sig/" . $_FILES["fileToUpload"]["name"] . " > sig.txt";
    system($code);
    system("cat sig.txt");
   # $output = file_get_contents("sig.txt");
    system("rm -rf sig.txt");
   # if((strpos($output,"It's a Signature") == True)) {
   #	 system("mv -v /var/www/html/uploads_sig/* /var/www/html/final/");
   #	}
  } else {
    echo "Sorry, there was an error uploading your file.";
  }
}
?>
