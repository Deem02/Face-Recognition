# import cv2
# import numpy as np
# from mtcnn import MTCNN
# from keras_facenet import FaceNet
# from sklearn.metrics.pairwise import cosine_similarity

# class FaceRecognition:
#     def __init__(self):
#         self.facenet = FaceNet()
#         self.detector = MTCNN()

#     def face_detection(self, image):
#         original_img = image
#         out = self.detector.detect_faces(original_img)

#         if out:
#             x, y, w, h = out[0]['box']
#             adjustment_factor_w = 0.2
#             adjustment_factor_h = 0.2
#             new_x = max(0, x - int(w * adjustment_factor_w))
#             new_y = max(0, y - int(h * adjustment_factor_h))
#             new_w = min(original_img.shape[1] - new_x, int(w * (1 + 2 * adjustment_factor_w)))
#             new_h = min(original_img.shape[0] - new_y, int(h * (1 + 2 * adjustment_factor_h)))

#             cropped_face = original_img[new_y:new_y + new_h, new_x:new_x + new_w]
#             return cropped_face
#         else:
#             return None

#     def preprocess_image(self, img):
#         img = cv2.resize(img, (160, 160))
#         img = np.expand_dims(img, axis=0)
#         return img

#     def get_face_embeddings(self, img):
#         img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         face_detect = self.face_detection(img)
#         if face_detect is not None:
#             img1 = self.preprocess_image(face_detect)
#             embeddings = self.facenet.embeddings(img1)
#             return embeddings
#         else:
#             return None

#     def compare_embeddings(self, user_embedding, stored_embeddings):
#         threshold = 0.56
#         for stored_embedding in stored_embeddings:
#             similarity = cosine_similarity(user_embedding, stored_embedding.reshape(1, -1))
#             if similarity > threshold:
#                 return True
#         return False

#     def display_image_with_caption(self, image, caption):
#         font = cv2.FONT_HERSHEY_SIMPLEX
#         org = (50, 50)
#         font_scale = 1.2
#         color = (0, 0, 255) if caption == "Authorized" else (255, 0, 0)
#         thickness = 1
#         img = cv2.putText(image, caption, org, font, font_scale, color, thickness, cv2.LINE_AA)
#         cv2.imshow('Face Detection', img)
#         cv2.waitKey(0)
#         cv2.destroyAllWindows()
