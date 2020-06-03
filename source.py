import moderngl
import moderngl_window as mglw
import numpy as np

ctx = moderngl.create_standalone_context()
class Test(mglw.WindowConfig):
    gl_version = (3, 3)
    window_size = (800, 600)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.prog = self.ctx.program(
            vertex_shader='''
                #version 330
                in vec2 in_vert;
                void main() {
                    gl_Position = vec4(in_vert, 0.0, 1.0);
                }
            ''',
            fragment_shader='''
                #version 330
                out vec4 f_color;
                void main() {
                    f_color = vec4(0.0, 0.0, 1.0, 1.0);
                }
            ''',
        )

        vertices = np.array([
            0.0, 0.8,
            -0.6, -0.8,
            0.6, -0.8,
        ])

        self.vbo = self.ctx.buffer(vertices.astype('f4').tobytes())
        self.vao = self.ctx.simple_vertex_array(self.prog, self.vbo, 'in_vert')

    def render(self, time, frametime):
        self.ctx.clear(0.0, 0.0, 0.0, 1.0)
        self.vao.render()


Test.run()
