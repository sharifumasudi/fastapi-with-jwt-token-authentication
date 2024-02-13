import models
from fastapi import HTTPException, status


class BlogRepository():
    def create_blog_post(db, request):
        blog = models.Blog(title=request.title, body=request.body, user_id=request.user_id)
        db.add(blog)
        db.commit()
        db.refresh(blog)
        return blog
    
    def get_all_blog(db):
        blogs = db.query(models.Blog).all()
        return blogs
    
    def get_blog(db, id: int):
        blog = db.query(models.Blog).filter(models.Blog.id == id).first()
        if not blog:
            # response.status_code = status.HTTP_404_NOT_FOUND
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No record found!")
            # return {"message": "No record found!"}
        return blog
    
    def delete_blog(db, id: int, response):
        blog = db.query(models.Blog).filter(models.Blog.id == id).first()
        if not blog:
            response.status_code = status.HTTP_404_NOT_FOUND
            return {"message": "No record found!"}
        db.delete(blog)
        db.commit()
        return "Blog deleted successfully"
    
    def update_blog(db, id: int, request, response):
        blog =   db.query(models.Blog).filter(models.Blog.id == id)
        if not blog.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
        else:    
            blog.update({models.Blog.title:request.title, models.Blog.body: request.body})
            db.commit()
            response.status_code = status.HTTP_202_ACCEPTED
            return {"msg": "Updated successfully"}