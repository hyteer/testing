import base64

token = "eyJhbGciOiJIUzI1NiIsImV4cCI6MTQ3MzY1MTEzNCwiaWF0IjoxNDczNjQ3NTM0fQ." \
        "eyJpZCI6M30.R2wOKcG7NP3l69KGNfxtHYPyocAaZ4BUsQN6B0Q_-UM:"
coded = base64.b64encode(token)
print coded

