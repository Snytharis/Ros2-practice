import rclpy
from rclpy.node import Node
from my_interfaces.msg import RobotStatus
from my_interfaces.srv import SetSpeedLimit
from std_srvs.srv import Trigger

class FakeRobot(Node):
    def __init__(self):
        super().__init__('fake_robot')
        
       
        self.publisher_ = self.create_publisher(RobotStatus, '/robot_status', 10)
        self.timer = self.create_timer(1.0, self.timer_callback) # 1.0 saniye = 1 Hz
        
        
        self.battery = 100.0
        self.speed = 1.0
        self.emergency_stop = False
        
       
        self.srv_speed = self.create_service(
            SetSpeedLimit, '/set_speed_limit', self.set_speed_limit_callback)
        self.srv_battery = self.create_service(
            Trigger, '/reset_battery', self.reset_battery_callback)
            
        self.get_logger().info('Sahte Robot Düğümü ve Servisleri Başlatıldı.')

    def timer_callback(self):
        msg = RobotStatus()
        msg.name = 'SahteRobot_v1'
        msg.battery = self.battery
        msg.speed = self.speed
        msg.emergency_stop = self.emergency_stop
        msg.stamp = self.get_clock().now().to_msg()
        
        self.publisher_.publish(msg)
        self.get_logger().info(f'Yayınlandı -> Batarya: %{self.battery:.1f} | Hız: {self.speed} m/s')
        
       
        if self.battery > 0.0:
            self.battery -= 1.5
            if self.battery < 0.0:
                self.battery = 0.0

    def set_speed_limit_callback(self, request, response):
        
        if 0.0 <= request.limit <= 2.0:
            self.speed = request.limit
            response.success = True
            response.message = f'Başarılı: Hız limiti {request.limit} m/s olarak güncellendi.'
            self.get_logger().info(response.message)
        else:
            response.success = False
            response.message = f'HATA: {request.limit} m/s geçersiz! Limit 0.0 ile 2.0 m/s arasında olmalıdır.'
            self.get_logger().warn(response.message)
        return response

    def reset_battery_callback(self, request, response):
        self.battery = 100.0
        response.success = True
        response.message = 'Batarya %100 seviyesine sıfırlandı.'
        self.get_logger().info(response.message)
        return response

def main(args=None):
    rclpy.init(args=args)
    node = FakeRobot()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()