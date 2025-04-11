from django.dispatch import Signal, receiver

# Define a custom signal
post_viewed = Signal()


@receiver(post_viewed, sender='portfolio.Post')
def increment_post_views(sender, instance, **kwargs):
    instance.views += 1
    instance.save(update_fields=['views'])
