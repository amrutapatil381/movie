import streamlit as st
import random
import string
from datetime import datetime

def generate_ticket_id():
    """Generate a random ticket ID."""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

def main():
    st.title("🎬 Movie Ticket Booking System")
    
    # Movie selection
    movies = ["Dune: Part Two", "Avatar 3", "Spider-Man: Beyond the Spider-Verse", "Oppenheimer"]
    movie = st.selectbox("Select a movie:", movies)
    
    # Date selection
    date = st.date_input("Select the date:", min_value=datetime.today())
    
    # Show timing selection
    timings = ["10:00 AM", "1:00 PM", "4:00 PM", "7:00 PM", "10:00 PM"]
    timing = st.selectbox("Select show timing:", timings)
    
    # Seat selection (basic implementation)
    seats = [f"Seat {i}" for i in range(1, 21)]
    selected_seats = st.multiselect("Select your seats (Max 5 seats per booking):", seats, max_selections=5)
    
    # Booking confirmation
    if st.button("Book Tickets"):
        if selected_seats:
            ticket_id = generate_ticket_id()
            st.success(f"✅ Booking Confirmed! Your Ticket ID: {ticket_id}")
            st.write(f"**Movie:** {movie}")
            st.write(f"**Date:** {date.strftime('%Y-%m-%d')}")
            st.write(f"**Time:** {timing}")
            st.write(f"**Seats:** {', '.join(selected_seats)}")
            st.write("Enjoy your movie! 🎥🍿")
        else:
            st.error("Please select at least one seat to proceed with booking.")

if __name__ == "__main__":
    main()
