import rclpy
from rclpy.node import Node
from my_interfaces.msg import RobotStatus

class Monitor(Node):
    def __init__(self):
        super().__init__('monitor')
        
        self.subscription = self.create_subscription(
            RobotStatus,
            '/robot_status',
            self.listener_callback,
            10
        )
        self.get_logger().info('Monitör Düğümü Başlatıldı.')

    def listener_callback(self, msg):
       
        if msg.battery < 20.0:
            self.get_logger().warn(
                f'DÜŞÜK BATARYA UYARISI! Robot: {msg.name} | Kalan Batarya: %{msg.battery:.1f}'
            )
        else:
            self.get_logger().info(f'Durum Normal | Batarya: %{msg.battery:.1f}')

def main(args=None):
    rclpy.init(args=args)
    node = Monitor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()