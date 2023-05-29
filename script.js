$(document).ready(function() {
  $('.dropdown-button').click(function() {
    $('.dropdown-menu').toggle();
  });
  
  $('.back-button').click(function() {
    history.back();
  });

  $('.edit-button').click(function() {
    $('#edit-icon1').show();
    $('#edit-icon2').show();
    $('#edit-icon3').show();
    $('#edit-icon4').show();
    $(this).hide(); // Hide the Edit button
    $('.save-button').show(); // Show the Save button
    $('#profile-picture-input').prop('disabled', false); // Enable profile picture input field
  });

  function updateProfilePictureEditability() {
    var editingMode = $('#profile-picture-container').hasClass('editing-mode');
    $('#profile-picture-input').prop('disabled', !editingMode);
  }

  $('.edit-icons').click(function() {
    var inputField = $(this).prev('.user-input');
    inputField.removeAttr('readonly');
    inputField.focus();
  });

  $('.save-button').click(function() {
    $('.user-input').attr('readonly', 'readonly');
    $('#edit-icon1').hide();
    $('#edit-icon2').hide();
    $('#edit-icon3').hide();
    $('#edit-icon4').hide();
    $(this).hide(); // Hide the Save button
    $('.edit-button').show(); // Show the Edit button
    $('#profile-picture-input').prop('disabled', true); // Disable profile picture input field
    updateProfilePictureEditability();
  });

  // Initialize profile picture input field as disabled
  $('#profile-picture-input').prop('disabled', true);

  $('#profile-picture-input').change(function(e) {
    var file = e.target.files[0];
    if (file) {
      var reader = new FileReader();
      reader.onload = function() {
        var imageUrl = reader.result;
        $('#profile-picture').attr('src', imageUrl);
      };
      reader.readAsDataURL(file);
    }
  });
});
