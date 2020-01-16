#利用Event类模拟红绿灯
import threading
import time



def lighter():
    green_time = 5       # 绿灯时间
    red_time = 5         # 红灯时间
    event.set()          # 初始设为绿灯
    while True:
        print("绿灯亮...")
        time.sleep(green_time)
        event.clear()
        print("红灯亮...")
        time.sleep(red_time)
        event.set()

def run(name):
    while True:
        if event.is_set():      # 判断当前是否"放行"状态
            print("一辆[%s] 呼啸开过..." % name)
            time.sleep(1)
        else:
            print("一辆[%s]开来，看到红灯，无奈的停下了..." % name)
            event.wait()
            print("[%s] 看到绿灯亮了，瞬间飞起....." % name)

if __name__ == '__main__':
    event = threading.Event()
    light = threading.Thread(target=lighter,)
    light.start()

    for name in ['奔驰', '宝马', '奥迪']:
        car = threading.Thread(target=run, args=(name,))
        car.start()
    '''
    【输出结果】：
    绿灯亮...
    一辆[奔驰] 呼啸开过...
    一辆[宝马] 呼啸开过...
    一辆[奥迪] 呼啸开过...
    一辆[奔驰] 呼啸开过...
    一辆[宝马] 呼啸开过...
    一辆[奥迪] 呼啸开过...
    一辆[宝马] 呼啸开过...
    一辆[奥迪] 呼啸开过...
    一辆[奔驰] 呼啸开过...
    一辆[宝马] 呼啸开过...
    一辆[奥迪] 呼啸开过...
    一辆[奔驰] 呼啸开过...
    一辆[奥迪] 呼啸开过...
    一辆[宝马] 呼啸开过...
    一辆[奔驰] 呼啸开过...
    红灯亮...
    一辆[奔驰]开来，看到红灯，无奈的停下了...
    一辆[奥迪]开来，看到红灯，无奈的停下了...
    一辆[宝马]开来，看到红灯，无奈的停下了...
    绿灯亮...
    [奔驰] 看到绿灯亮了，瞬间飞起.....
    [奥迪] 看到绿灯亮了，瞬间飞起.....
    一辆[奔驰] 呼啸开过...
    一辆[奥迪] 呼啸开过...
    [宝马] 看到绿灯亮了，瞬间飞起.....
    一辆[宝马] 呼啸开过...
    一辆[奥迪] 呼啸开过...
    一辆[宝马] 呼啸开过...
    一辆[奔驰] 呼啸开过...
    一辆[奥迪] 呼啸开过...
    一辆[奔驰] 呼啸开过...
    一辆[宝马] 呼啸开过...
    一辆[宝马] 呼啸开过...
    一辆[奥迪] 呼啸开过...
    一辆[奔驰] 呼啸开过...
    一辆[奔驰] 呼啸开过...
    一辆[奥迪] 呼啸开过...
    一辆[宝马] 呼啸开过...
    红灯亮...
    一辆[奥迪]开来，看到红灯，无奈的停下了...
    一辆[奔驰]开来，看到红灯，无奈的停下了...
    一辆[宝马]开来，看到红灯，无奈的停下了...
    '''