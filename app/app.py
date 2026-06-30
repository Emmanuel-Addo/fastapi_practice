from fastapi import FastAPI, HTTPException
import app.schemas import PostCreate

app = FastAPI()

text_posts = {
  1: {
    "title": "Getting Started with React",
    "content": "React makes it easy to build fast and interactive user interfaces using reusable components."
  },
  2: {
    "title": "Understanding JavaScript",
    "content": "JavaScript is the backbone of modern web development, powering dynamic and interactive websites."
  },
  3: {
    "title": "Learning Tailwind CSS",
    "content": "Tailwind CSS helps developers build beautiful and responsive interfaces with utility-first classes."
  },
  4: {
    "title": "Why Learn Node.js?",
    "content": "Node.js allows developers to build scalable server-side applications using JavaScript."
  },
  5: {
    "title": "Exploring Firebase",
    "content": "Firebase provides authentication, real-time databases, cloud storage, and hosting for web applications."
  },
  6: {
    "title": "Version Control with Git",
    "content": "Git makes it easy to track changes, collaborate with others, and manage project history."
  },
  7: {
    "title": "Building REST APIs",
    "content": "REST APIs enable communication between frontend and backend applications using HTTP requests."
  },
  8: {
    "title": "MongoDB Basics",
    "content": "MongoDB is a flexible NoSQL database that stores data in JSON-like documents."
  },
  9: {
    "title": "Deploying Your App",
    "content": "Deploy your full-stack application using platforms like Vercel, Render, or Railway for public access."
  },
  10: {
    "title": "Becoming a Better Developer",
    "content": "Consistent practice, building real-world projects, and learning from feedback are key to becoming a skilled software developer."
  }
}

@app.get("/posts")
def get_all_post(limit: int = None):
    if limit:
        return text_posts[:limit]
    return text_posts

@app.get("/posts/{id}")
def get_post(id: init):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Past not found")
    return text_posts.get(id)

@app.post("/posts")
def create_post(post: PostCreate):
    text_posts[max(text_posts.keys()) + 1] = {"title": post.title, "content":post.content}