'use client'; // This directive is important for Next.js client components

import React, { useState, useRef, useEffect } from 'react';
import { Send, MessageSquare } from 'lucide-react'; // Importing icons from lucide-react

interface Message {
  id: string;
  text: string;
  sender: 'user' | 'ai';
}

export default function Home() {

  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState<string>('');
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  // Scroll to the bottom of the chat on new messages
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);


  // Function to simulate AI response
  const getAiResponse = async (userMessage: string): Promise<string> => {
    setIsLoading(true);
    // Simulate API call delay
    await new Promise(resolve => setTimeout(resolve, 1000));

    // Example of using the Gemini API (uncomment and replace with actual logic)
    let chatHistory = [];
    chatHistory.push({ role: "user", parts: [{ text: userMessage }] });
    const payload = { contents: chatHistory };
    const apiKey = ""; // Canvas will provide this at runtime
    const apiUrl = `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=${apiKey}`;

    try {
      const response = await fetch(apiUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });
      const result = await response.json();
      if (result.candidates && result.candidates.length > 0 &&
          result.candidates[0].content && result.candidates[0].content.parts &&
          result.candidates[0].content.parts.length > 0) {
        return result.candidates[0].content.parts[0].text;
      } else {
        return "Sorry, I couldn't get a response from the AI.";
      }
    } catch (error) {
      console.error("Error calling Gemini API:", error);
      return "There was an error connecting to the AI. Please try again.";
    } finally {
      setIsLoading(false);
    }

    // Mock AI response for demonstration
    // const lowerCaseMessage = userMessage.toLowerCase();
    // if (lowerCaseMessage.includes('hello') || lowerCaseMessage.includes('hi')) {
    //   return 'Hello there! How can I help you today?';
    // } else if (lowerCaseMessage.includes('how are you')) {
    //   return 'I am just a program, but I am functioning well! Thanks for asking.';
    // } else if (lowerCaseMessage.includes('name')) {
    //   return 'I am a chatbot created to assist you.';
    // } else if (lowerCaseMessage.includes('help')) {
    //   return 'I can answer questions, provide information, or just chat. What do you need help with?';
    // } else {
    //   return "I'm not sure how to respond to that. Can you please rephrase your question?";
    // }
  };

  // Handle sending a message
  const handleSendMessage = async () => {
    if (input.trim() === '') return;

    const newUserMessage: Message = {
      id: Date.now().toString() + '-user',
      text: input,
      sender: 'user',
    };
    setMessages(prevMessages => [...prevMessages, newUserMessage]);
    setInput('');

    const aiResponseText = await getAiResponse(input);
    const newAiMessage: Message = {
      id: Date.now().toString() + '-ai',
      text: aiResponseText,
      sender: 'ai',
    };
    setMessages(prevMessages => [...prevMessages, newAiMessage]);
    setIsLoading(false);
  };

  // Handle Enter key down
  const handleKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter' && !isLoading) {
      handleSendMessage();
    }
  };

  return (
    <div className="flex flex-col h-screen bg-gray-50 font-sans p-4 sm:p-6 md:p-8 rounded-lg shadow-xl max-w-4xl mx-auto my-4 border border-gray-200">
      {/* Header */}
      <div className="flex items-center justify-center mb-6 py-3 bg-white rounded-lg shadow-sm border border-gray-100">
        <MessageSquare className="w-8 h-8 text-blue-500 mr-3" />
        <h1 className="text-3xl sm:text-2xl font-semibold text-gray-800">
          AI Chatbot
        </h1>
      </div>

      {/* Chat History Display */}
      <div className="flex-1 overflow-y-auto p-4 space-y-4 bg-white rounded-lg shadow-inner mb-6 border border-gray-200">
        {messages.length === 0 && (
          <div className="text-center text-gray-400 italic mt-10 text-lg">
            Start a conversation by typing a message below!
          </div>
        )}
        {messages.map((message) => (
          <div
            key={message.id}
            className={`flex ${message.sender === 'user' ? 'justify-end' : 'justify-start'
              }`}
          >
            <div
              className={`max-w-[75%] px-4 py-1 rounded-lg shadow-sm text-sm sm:text-md ${message.sender === 'user'
                  ? 'bg-blue-500 text-white rounded-br-none'
                  : 'bg-gray-100 text-gray-800 rounded-bl-none'
                }`}
            >
              <p className="break-words">{message.text}</p>
            </div>
          </div>
        ))}
        {isLoading && (
          <div className="flex justify-start">
            <div className="max-w-[75%] px-4 py-2 rounded-lg shadow-sm bg-gray-100 text-gray-800 rounded-bl-none">
              <div className="flex items-center space-x-2">
                <div className="w-2 h-2 bg-gray-500 rounded-full animate-bounce delay-0"></div>
                <div className="w-2 h-2 bg-gray-500 rounded-full animate-bounce delay-75"></div>
                <div className="w-2 h-2 bg-gray-500 rounded-full animate-bounce delay-150"></div>
              </div>
            </div>
          </div>
        )}
        <div ref={messagesEndRef} /> {/* Scroll target */}
      </div>

      {/* Message Input Area */}
      <div className="flex items-center p-3 bg-white rounded-lg shadow-md border border-gray-200">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Type your message..."
          className="flex-1 py-1 px-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-300 text-base sm:text-md transition-all duration-200"
          disabled={isLoading}
        />
        <button
          onClick={handleSendMessage}
          className={`ml-2 px-3 py-1 bg-gradient-to-r from-blue-500 to-blue-700 text-white font-semibold rounded-lg shadow-md flex items-center justify-center transition-all duration-300 ease-in-out cursor-pointer
            ${isLoading ? 'opacity-60 cursor-not-allowed' : 'hover:from-blue-600 hover:to-blue-800 active:from-blue-700 active:to-blue-900 transform hover:scale-105'}
          `}
          disabled={isLoading}
        >
          {isLoading ? (
            <span className="text-sm">Sending...</span>
          ) : (
            <>
              <Send className="w-5 h-5 mr-2" />
              <span className="hidden sm:inline">Send</span>
            </>
          )}
        </button>
      </div>
    </div>
  );
}
