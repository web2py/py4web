var enable_firebase_push = function(vapid_key, send_token_to_server, on_message) {
    // enable messaging
    const messaging = firebase.messaging();
    // what to do when a message is received
    messaging.onMessage(function(payload) {
            on_message(payload);
        });
    // what todo when we have a new token
    messaging.getToken({vapidKey: vapid_key})
    .then(function(currentToken) {
        if (currentToken) {
            if(window.localStorage.getItem('firebase-push-token-sent') !== 'T') {
                send_token_to_server(currentToken);
            }
            window.localStorage.setItem('firebase-push-token-sent', 'T');
        } else {
            window.localStorage.setItem('firebase-push-token-sent', 'F');
        }
    }).catch(function(erro) {
        window.localStorage.setItem('firebase-push-token-sent', 'F');
    });
}