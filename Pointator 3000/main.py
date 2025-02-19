from controller.controller import controller
from models.model import model
from models.point import point
from views.view import view


def main():
    # Initialize the model
    model_instance = model.Model()
    
    # Initialize the view with the controller
    view_instance = view.View(controller_instance)

    # Initialize the controller with the model
    controller_instance = controller.Controller(model_instance)
    controller_instance.set_view(view_instance)
    
    # Start the application
    view_instance.run()

if __name__ == "__main__":
    main()