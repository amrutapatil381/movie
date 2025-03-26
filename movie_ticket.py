import streamlit as st
import random
import string
import pdfkit
from datetime import datetime
from io import BytesIO

def generate_ticket_id():
    """Generate a random ticket ID."""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

def generate_ticket_pdf(ticket_details):
    """Generate a PDF for the booked ticket."""
    ticket_html = f"""
    <h2>Movie Ticket</h2>
    <p><strong>Ticket ID:</strong> {ticket_details['ticket_id']}</p>
    <p><strong>Name:</strong> {ticket_details['name']}</p>
    <p><strong>Email:</strong> {ticket_details['email']}</p>
    <p><strong>Movie:</strong> {ticket_details['movie']}</p>
    <p><strong>Theater:</strong> {ticket_details['theater']}</p>
    <p><strong>Date:</strong> {ticket_details['date']}</p>
    <p><strong>Time:</strong> {ticket_details['timing']}</p>
    <p><strong>Seats:</strong> {', '.join(ticket_details['seats'])}</p>
    <p><strong>Total Price:</strong> ${ticket_details['total_price']}</p>
    <p>Enjoy your movie! 🎥🍿</p>
    """
    pdf = pdfkit.from_string(ticket_html, False)
    return pdf

def main():
    st.title("🎬 Advanced Movie Ticket Booking System")
    
    # Theater selection
    theaters = ["IMAX Downtown", "Cinema City Mall", "Regal Theaters", "PVR Platinum"]
    theater = st.selectbox("Select a theater:", theaters)
    
    # Movie selection
    movies = ["Dune: Part Two", "Avatar 3", "Spider-Man: Beyond the Spider-Verse", "Oppenheimer"]
    movie = st.selectbox("Select a movie:", movies)
    
    # Date selection
    date = st.date_input("Select the date:", min_value=datetime.today())
    
    # Show timing selection
    timings = ["10:00 AM", "1:00 PM", "4:00 PM", "7:00 PM", "10:00 PM"]
    timing = st.selectbox("Select show timing:", timings)
    
    # User details
    name = st.text_input("Enter your name:")
    email = st.text_input("Enter your email:")
    
    # Seat selection with pricing
    seats = {f"Seat {i}": random.randint(10, 20) for i in range(1, 21)}  # Dynamic pricing
    selected_seats = st.multiselect("Select your seats (Max 5 seats per booking):", list(seats.keys()), max_selections=5)
    
    total_price = sum(seats[s] for s in selected_seats)
    
    if selected_seats:
        st.write(f"Total Price: **${total_price}**")
    
    # Booking confirmation
    if st.button("Book Tickets"):
        if selected_seats and name and email:
            ticket_id = generate_ticket_id()
            ticket_details = {
                "ticket_id": ticket_id,
                "name": name,
                "email": email,
                "movie": movie,
                "theater": theater,
                "date": date.strftime('%Y-%m-%d'),
                "timing": timing,
                "seats": selected_seats,
                "total_price": total_price,
            }
            
            st.success(f"✅ Booking Confirmed! Your Ticket ID: {ticket_id}")
            st.write(f"**Movie:** {movie}")
            st.write(f"**Theater:** {theater}")
            st.write(f"**Date:** {ticket_details['date']}")
            st.write(f"**Time:** {timing}")
            st.write(f"**Seats:** {', '.join(selected_seats)}")
            st.write(f"**Total Price:** ${total_price}")
            st.write("Enjoy your movie! 🎥🍿")
            
            # Generate and provide PDF download
            pdf_bytes = generate_ticket_pdf(ticket_details)
            st.download_button("Download Ticket", data=pdf_bytes, file_name=f"Ticket_{ticket_id}.pdf", mime="application/pdf")
        else:
            st.error("Please fill in all details and select at least one seat.")

if __name__ == "__main__":
    main()
