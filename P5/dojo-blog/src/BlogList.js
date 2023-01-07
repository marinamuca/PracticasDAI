import BlogInfo from "./BlogInfo";

const BlogList = ({blogs, title, handleDelete}) => {
    return (
        <div className="blog-list">
            <h2>{ title }</h2>
            {blogs.map((blog) => (
                <BlogInfo blog={blog} handleDelete={handleDelete} key={blog.id}/>
            ))}
        </div>
    );
}
 
export default BlogList;