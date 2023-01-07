import BlogPreview from "./BlogPreview";
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

const BlogList = ({blogs, title, handleDelete}) => {
    return (
        <div className="blog-list">
            <h2>{title}</h2>
            <Container>
                <Row>
                    {blogs.map((blog) => (
                        <Col xs={6}>
                            <BlogPreview blog={blog} handleDelete={handleDelete} key={blog.id} />
                        </Col>
                    ))}
                </Row>
            </Container> 
        </div>
    );
}
 
export default BlogList;