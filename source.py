import moderngl_window as mglw

class Test(mglw.WindowConfig):
    gl_version = (3, 3)
    window_size = (200, 200)
    def render(self, time, frametime):
        self.ctx.clear(0.0, 0.0, 1.0, 0.0)



mglw.run_window_config(Test)


