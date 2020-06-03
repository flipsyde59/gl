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
                in vec2 a_position;
                in float a_t;
                out float v_t;
                void main() {
                    v_t=a_t
                    gl_Position = vec4(a_position, 0.0, 1.0);
                }
            ''',
            fragment_shader='''
                #version 330
                in float v_t;
                out vec4 o_color;
                void main() {
                    o_color = vec4(sin(v_t*62.83), 0.0, 0.0, 1.0);
                }
            ''',
        )

        vertices = np.array([
            0.5, 0.5,
            -0.5, -0.5,
            0.5, -0.5,
            -0.5, 0.5
        ])

        self.vbo = self.ctx.buffer(vertices.astype('f4').tobytes())
        self.vao = self.ctx.simple_vertex_array(self.prog, self.vbo, 'in_vert', 'in_color')

    def render(self, time, frametime):
        self.ctx.clear(0.0, 0.0, 0.0, 1.0)
        self.vao.render()


Test.run()
