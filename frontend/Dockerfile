# Use Node 20 on Debian slim (for glibc compatibility with lightningcss)
FROM node:20-slim AS base

# Set working directory
WORKDIR /app

# Install dependencies only when needed
FROM base AS deps
COPY package.json package-lock.json* ./
RUN npm ci

# Build the application
FROM base AS builder
WORKDIR /app

# Install build tools for native dependencies
RUN apt-get update && apt-get install -y build-essential python3 rustc cargo && rm -rf /var/lib/apt/lists/*

# Copy app source and dependencies
COPY . .
COPY --from=deps /app/node_modules ./node_modules

# Rebuild native modules to match container environment
RUN npm rebuild lightningcss

RUN npm run build

# Production image
FROM base AS runner
WORKDIR /app

ENV NODE_ENV=production

# Copy exported static files (Next.js exports to 'out' directory)
COPY --from=builder /app/out ./out

# Simple HTTP server to serve static files
RUN npm install -g serve
CMD ["serve", "-s", "out", "-l", "3000"]

# Expose port 3000
EXPOSE 3000
