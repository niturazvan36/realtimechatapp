document.querySelector('#room-name-input').focus();
        document.querySelector('#room-name-input').onkeyup = function(e) {
            if (e.keyCode === 13) {  // enter, return
                document.querySelector('#room-name-input').click();
            }
        };
        document.querySelector('#room-name-input').onclick = function(e) {
            var roomName = document.querySelector('#room-name-input').value;
            window.location.pathname = roomName + '/';
        };