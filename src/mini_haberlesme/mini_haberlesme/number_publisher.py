import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import random
from rclpy.qos import QoSProfile, ReliabilityPolicy, DurabilityPolicy

class NumberPublisher(Node):
    def __init__(self):
        super().__init__('number_publisher')
        
        \
        qos_profile = QoSProfile(
            depth=10,
            reliability=ReliabilityPolicy.RELIABLE,
            durability=DurabilityPolicy.TRANSIENT_LOCAL
        )
        
        self.publisher_ = self.create_publisher(Int32, '/number', qos_profile)
        self.timer = self.create_timer(0.5, self.timer_callback)

    def timer_callback(self):
        msg = Int32()
        msg.data = random.randint(1, 100)
        self.publisher_.publish(msg)
        self.get_logger().info(f'Yayınlanan sayı: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = NumberPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()