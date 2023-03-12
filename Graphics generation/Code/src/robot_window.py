import moderngl
import numpy as np
from pyrr import Matrix44, Vector3
from base_window import BaseWindowConfig


class RobotWindow(BaseWindowConfig):

    def __init__(self, **kwargs):
        super(RobotWindow, self).__init__(**kwargs)

    def model_load(self):
        self.cube = self.load_scene('cube.obj')
        self.cube = self.cube.root_nodes[0].mesh.vao.instance(self.program)

        self.sphere = self.load_scene('sphere.obj')
        self.sphere = self.sphere.root_nodes[0].mesh.vao.instance(self.program)

    def init_shaders_variables(self):
        self.color = self.program['color']
        self.mvp = self.program['mvp']

    def render(self, time: float, frame_time: float):
        self.ctx.clear(0.8, 0.8, 0.8, 0.0)
        self.ctx.enable(moderngl.DEPTH_TEST)

        projection = Matrix44.perspective_projection(45.0, self.aspect_ratio, 0.1, 1000.0)
        lookat = Matrix44.look_at(
            (-20.0, -15.0, 5.0),
            (0.0, 0.0, 1.0),
            (0.0, 0.0, 1.0),
        )


        self.color.value = (0.155, 0.50, 0.200) #kolor
        move = Matrix44.from_translation((0.0, 0.0, 5.0)) #translacja
        self.mvp.write((projection * lookat * move).astype('float32')) #zapisanie macierzy z translacjami do mvp
        self.sphere.render() #Rendering glowy

        self.color.value = (0.955, 0.400, 0.200)
        move = Matrix44.from_translation((0.0, 0.0, 2.0))
        scale = Matrix44.from_scale((1.0, 1.0, 2.0)) #skalowanie
        self.mvp.write((projection * lookat * move * scale).astype('float32'))
        self.cube.render() #render ciala

        self.color.value = (0.255, 0.80, 0.800)
        move = Matrix44.from_translation((0.0, -3.0, 3.0))
        rotate = Matrix44.from_x_rotation(0.25 * np.pi) #rotacja
        scale = Matrix44.from_scale(Vector3([0.5, 0.5, 1.25])) #skalowanie
        self.mvp.write((projection * lookat * move * rotate * scale).astype('float32'))
        self.cube.render() #render lewej reki

        self.color.value = (0.255, 0.80, 0.800)
        move = Matrix44.from_translation(Vector3([0.0, 3.0, 3.0]))
        rotate = Matrix44.from_x_rotation(-0.25 * np.pi)
        scale = Matrix44.from_scale(Vector3([0.5, 0.5, 1.25]))
        self.mvp.write((projection * lookat * move * rotate * scale).astype('float32'))
        self.cube.render() #render prawej reki

        self.color.value = (1.0, 1.0, 0.0)
        move = Matrix44.from_translation((0.0, 2.0, -1.5))
        scale = Matrix44.from_scale((0.5, 0.5, 1.75))
        rotate = Matrix44.from_x_rotation(np.pi / -6)
        self.mvp.write((projection * lookat * move * rotate * scale).astype('float32'))
        self.cube.render() #render lewej nogi


        self.color.value = (1.0, 1.0, 0.0)
        move = Matrix44.from_translation((0.0, -2.0, -1.5))
        scale = Matrix44.from_scale((0.5, 0.5, 1.75))
        rotate = Matrix44.from_x_rotation(np.pi / 6)
        self.mvp.write((projection * lookat * move * rotate * scale).astype('float32'))
        self.cube.render() #render prawej nogi
