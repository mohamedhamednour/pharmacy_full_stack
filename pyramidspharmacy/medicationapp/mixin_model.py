from django_lifecycle import (
    AFTER_SAVE,
    LifecycleModelMixin,
    hook,
)





class RefillRequestMixin(LifecycleModelMixin):

    @hook(AFTER_SAVE)
    def check_quantity(self):

     
        if self.medication.quantity >= self.quantity:
            self.medication.quantity -=self.quantity 
            self.medication.save()
        else:
            raise ValueError('The quantity of medication is not enough for the refill request')

        

        

        