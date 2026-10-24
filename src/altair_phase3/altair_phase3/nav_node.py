import rclpy
from rclpy.node import Node
from std_srvs.srv import SetBool

class RoverNavNode(Node):
    def __init__(self):
        super().__init__('rover_nav')
        # Service server to enable/disable autonomous navigation mode
        self.srv = self.create_service(SetBool, 'toggle_navigation', self.navigation_callback)
        self.get_logger().info('Rover Navigation Service Node is ready.')

    def navigation_callback(self, request, response):
        if request.data:
            response.success = True
            response.message = "Autonomous navigation ENABLED."
            self.get_logger().info('Navigation state updated: ENABLED')
        else:
            response.success = True
            response.message = "Autonomous navigation DISABLED."
            self.get_logger().info('Navigation state updated: DISABLED')
        return response

def main(args=None):
    rclpy.init(args=args)
    node = RoverNavNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

