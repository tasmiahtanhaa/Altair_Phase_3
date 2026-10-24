import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class RoverTelemetryNode(Node):
    def __init__(self):
        super().__init__('rover_telemetry')
        self.publisher_ = self.create_publisher(String, 'rover_telemetry', 10)
        timer_period = 1.0  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.get_logger().info('Rover Telemetry Node has been started.')

    def timer_callback(self):
        msg = String()
        msg.data = "STATUS: OK | Battery: 12.4V | Temp: 32.5C | Mode: Autonomous"
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    node = RoverTelemetryNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

