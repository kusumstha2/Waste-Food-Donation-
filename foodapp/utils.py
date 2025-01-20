from geopy.distance import geodesic
from django.core.mail import send_mail
from django.conf import settings
from sklearn.neighbors import NearestNeighbors
import numpy as np

def calculate_distance(lat1, lon1, lat2, lon2):
    """Calculate the geodesic distance between two points."""
    return geodesic((lat1, lon1), (lat2, lon2)).km

# foodapp/utils.py

def notify_recipients(subject, message, recipient_list):
    """
    Function to notify recipients via email.
    :param subject: Subject of the email.
    :param message: Message body of the email.
    :param recipient_list: List of email addresses to notify.
    """
    try:
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            recipient_list,
            fail_silently=False,
        )
        print(f"Successfully sent email to: {', '.join(recipient_list)}")
    except Exception as e:
        print(f"Error sending email: {e}")

# foodapp/utils.py



import numpy as np
from sklearn.neighbors import NearestNeighbors

def knn_recipients(location, recipients, k=5):
    """
    Function to find the nearest k recipients based on location using KNN.
    :param location: Tuple (lat, lon) of the donor.
    :param recipients: List of recipient locations, each a tuple (id, (lat, lon)).
    :param k: Number of nearest neighbors to return.
    :return: List of the nearest k recipients.
    """
    # Convert locations into an array for NearestNeighbors
    locations = np.array([recipient[1] for recipient in recipients])  # Assuming recipients are (id, (lat, lon))
    
    model = NearestNeighbors(n_neighbors=k)
    model.fit(locations)
    distances, indices = model.kneighbors([location])

    # Return the nearest recipients' ids
    nearest_recipients = [recipients[i][0] for i in indices[0]]
    return nearest_recipients
