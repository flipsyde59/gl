import moderngl_window as mglw
import numpy as np


class Test(mglw.WindowConfig):
    gl_version = (3, 3)
    window_size = (800, 600)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.prog = self.ctx.program(
            vertex_shader='''
                #version 330

                layout(location = 0) in vec2 a_position;
                layout(location = 1) in vec3 a_color;

                out vec3 v_color;

                void main()
                {
                    gl_Position = vec4(a_position, 0.0, 1.0);
                    v_color = a_color;
                }
                ''',
            fragment_shader='''
                #version 330

                in vec3 v_color;
                out vec4 out_color;
                
                void main()
                {
                    float r = v_color.r;
                    float g = v_color.g;
                    out_color = vec4(tan((sin(g*30)+r*20)*5), 0.0, 0.0, 0.0);
                }
                ''',
        )

        vertices = np.array([
            0.5, 0.5, 1.0, 0.0, 0.0,
            -0.5, 0.5, 1.0, 1.0, 0.0,
            -0.5, -0.5, 0.0, 1.0, 0.0,
            0.5, -0.5, 0.0, 0.0, 0.0,
        ])

        self.vbo = self.ctx.buffer(vertices.astype('f4').tobytes()*4)
        self.vao = self.ctx.simple_vertex_array(self.prog, self.vbo, 'a_position', 'a_color')

    def render(self, time, frametime):
        self.ctx.clear(0.0, 0.0, 0.0, 1.0)
        self.vao.render()


Test.run()
