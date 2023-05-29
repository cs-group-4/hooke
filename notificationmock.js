$(document).ready(function() {
  // Fetch the mock notifications data (assuming it's in a separate file)
  $.getJSON('mockData.js')
    .done(function(mockNotifications) {
      // Loop through each notification and create the corresponding HTML elements
      mockNotifications.forEach(function(notification) {
        var notificationItem = $('<div>').addClass('notification');
        var profilePicture = $('<img>').addClass('pfp-image');
        var pfpDiv = $('<div>').addClass('pfp-div');
        var senderName = $('<h1>').text(notification.sender);
        var message = $('<p>').text(notification.message);
        var timestamp = $('<p>').text(notification.timestamp);

        // Append the elements to the notification item
        pfpDiv.append(senderName, message, timestamp);
        notificationItem.append(profilePicture, pfpDiv);

        // Append the notification item to the notification container
        $('.notification-container').append(notificationItem);
      });
    })
    .fail(function() {
      console.error('Failed to fetch mock notifications data.');
    });
});
