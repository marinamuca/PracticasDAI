import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import Modal from 'react-bootstrap/Modal';
import { useState } from 'react'

const BlogPreview = ({blog, handleDelete}) => {
    const [show, setShow] = useState(false);

    const handleClose = () => setShow(false);
    const handleShow = () => setShow(true);

    return (
        <>
            <Card className='blog-preview' style={{ minWidth: '100%' }}>
                <Card.Body>
                    <Card.Title>
                        <h2>{blog.title}</h2>
                    </Card.Title>
                    <Card.Text>
                        <p>Written by {blog.author}</p>
                    </Card.Text>
                    <Button variant="danger" onClick={handleShow}>Delete Blog</Button>
                </Card.Body>
            </Card>

            <Modal show={show} onHide={handleClose} centered>
                <Modal.Header closeButton>
                    <Modal.Title>Are you Sure?</Modal.Title>
                </Modal.Header>
                <Modal.Body>
                    <p>Do you really want to delete {blog.title}?</p>
                </Modal.Body>
                <Modal.Footer>
                    <Button variant="secondary" onClick={handleClose}>Cancel</Button>
                    <Button variant="danger" onClick={() => handleDelete(blog.id)}>Delete Blog</Button>
                </Modal.Footer>
            </Modal>
        </>
    );
}

export default BlogPreview;