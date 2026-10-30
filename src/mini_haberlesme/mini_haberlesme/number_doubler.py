import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from rclpy.qos import QoSProfile, ReliabilityPolicy, DurabilityPolicy

class NumberDoubler(Node):
    def __init__(self):
        super().__init__('number_doubler')
        
        
        qos_profile = QoSProfile(
            depth=10,
            reliability=ReliabilityPolicy.RELIABLE,
            durability=DurabilityPolicy.TRANSIENT_LOCAL
        )
        
        self.subscription = self.create_subscription(
            Int32,
            '/number',
            self.listener_callback,
            qos_profile)
            
        self.publisher_ = self.create_publisher(Int32, '/number_doubled', 10)

    def listener_callback(self, msg):
        doubled_val = msg.data * 2
        self.get_logger().info(f'Alınan: {msg.data} | Çarpılan: {doubled_val}')
        
        out_msg = Int32()
        out_msg.data = doubled_val
        self.publisher_.publish(out_msg)

def main(args=None):
    rclpy.init(args=args)
    node = NumberDoubler()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()