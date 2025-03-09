
# profile 分析

使用 torch.profiler.profile 上下文管理器的时候
- 进入上下文的时候, 调用C++测的_enable_profiler方法(torch/csrc/autograd/profiler_kineto.h中enableProfiler方法), 向管理器注册回调(push???Callbacks方法, LocalCallbackManager) 
- tensor操作分发到具体kernel的时候, 获取注册的回调(aten/src/ATen/core/dispatch/Dispatcher.h文件中的inline void Dispatcher::callBoxed(const OperatorHandle& op, Stack* stack)方法), 输出相关信息执行该回调
- 退出上下文的时候, 调用C++测的_disable_profiler方法(torch/csrc/autograd/profiler_kineto.cpp中的enableProfiler方法)拿取结果


