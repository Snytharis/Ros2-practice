import sys
import rclpy
from rclpy.node import Node
from my_interfaces.srv import SetSpeedLimit

class SpeedLimitClient(Node):
    def __init__(self):
        super().__init__('speed_limit_client')
        self.cli = self.create_client(SetSpeedLimit, '/set_speed_limit')
        
  
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Servis bekleniyor, lütfen sunucuyu başlattığınızdan emin olun...')

    def send_request(self, limit_val):
        req = SetSpeedLimit.Request()
        req.limit = limit_val
        
       
        future = self.cli.call_async(req)
        return future

def main(args=None):
    rclpy.init(args=args)
    client = SpeedLimitClient()
    
   
    test_limit = 3.5 
    
    future = client.send_request(test_limit)
    
    
    rclpy.spin_until_future_complete(client, future)
    
    response = future.result()
    client.get_logger().info(
        f'Servis Cevabı Geldi -> Başarılı: {response.success} | Mesaj: "{response.message}"'
    )
    
    client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()