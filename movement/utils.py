from .models import Movement

def get_closed_movement(instance):
    if instance.status == 1:
            total_count_books = instance.books.count()
            count             = 0
            mov               = Movement.objects.filter(loan_id__iexact=instance.id)
        
            if len(mov) <= 0:
                return False

            for m in mov:
                count += m.books.count()

            if count == total_count_books:
                return True

    return False