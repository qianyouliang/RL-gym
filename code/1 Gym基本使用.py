import gymnasium as gym

# 创建环境
env = gym.make("LunarLander-v2", render_mode="human")
observation, info = env.reset()

# 与环境互动
for _ in range(1000):
    action = env.action_space.sample()  # 代理策略选择动作
    observation, reward, terminated, truncated, info = env.step(action)

    if terminated or truncated:
        observation, info = env.reset()

# 关闭环境
env.close()