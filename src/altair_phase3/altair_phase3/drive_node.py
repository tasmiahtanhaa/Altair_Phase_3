import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class RoverDriveNode(Node):
    def __init__(self):
        super().__init__('rover_drive')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.get_logger().info('Rover Drive Node has been started.')

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = 2.0  # Drive forward speed
        msg.angular.z = 1.8 # Turn speed
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing velocity -> Linear: {msg.linear.x}, Angular: {msg.angular.z}')

def main(args=None):
    rclpy.init(args=args)
    node = RoverDriveNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

