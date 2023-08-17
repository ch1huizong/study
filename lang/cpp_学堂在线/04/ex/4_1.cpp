#include <iostream>
// T: 类的组合，CPU类

enum CPU_Rank { P1 = 1, P2, P3, P4, P5, P6, P7 };

class CPU {
  public:
    CPU(CPU_Rank r, int f, float v) : rank(r), frequency(f), voltage(v) {
        std::cout << "构造了一个CPU！" << std::endl;
    };

    virtual ~CPU() { std::cout << "析构了一个CPU！" << std::endl; }

    CPU_Rank GetRank() const { return rank; };
    int GetFrequency() const { return frequency; };
    float GetVoltage() const { return voltage; };

    void SetRank(CPU_Rank r) { rank = r; };
    void SetFrequency(int f) { frequency = f; };
    void SetVoltage(float v) { voltage = v; };

    void Run() { std::cout << "CPU开始运行!" << std::endl; };
    void Stop() { std::cout << "CPU停止运行!" << std::endl; }

  private:
    CPU_Rank rank; // 等级
    int frequency;
    float voltage;
};

int main(int argc, char *argv[]) {
    CPU a(P6, 300, 2.8);
    a.Run();
    a.Stop();

    return 0;
}
