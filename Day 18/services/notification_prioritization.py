def prioritize_notifications(notifications):

    if not isinstance(notifications, list):

        return {
            "status": "error",
            "message": "Notifications must be provided as a list."
        }

    if not notifications:

        return {
            "status": "success",
            "total_notifications": 0,
            "notifications": [],
            "message": "No notifications available."
        }

    priority_scores = {
        "CRITICAL": 100,
        "HIGH": 80,
        "MEDIUM": 50,
        "LOW": 20
    }

    processed_notifications = []

    for notification in notifications:

        if not isinstance(notification, dict):

            continue

        title = notification.get(
            "title",
            "Untitled Notification"
        )

        message = notification.get(
            "message",
            ""
        )

        priority = str(
            notification.get(
                "priority",
                "LOW"
            )
        ).upper()

        # Unknown priority ko LOW treat karenge
        score = priority_scores.get(
            priority,
            20
        )

        processed_notifications.append({
            "title": title,
            "message": message,
            "priority": priority,
            "priority_score": score
        })

    # Highest priority first
    processed_notifications.sort(
        key=lambda item: item["priority_score"],
        reverse=True
    )

    # Add display order
    for index, notification in enumerate(
        processed_notifications,
        start=1
    ):

        notification["display_order"] = index

    # Top notification
    top_notification = (
        processed_notifications[0]
        if processed_notifications
        else None
    )

    return {
        "status": "success",
        "total_notifications": len(
            processed_notifications
        ),
        "notifications": processed_notifications,
        "top_priority_notification": top_notification
    }