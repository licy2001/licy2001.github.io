import { defineCollection, z } from 'astro:content';

const posts = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    published: z.coerce.date(),
    tags: z.array(z.string()).default([]),
    category: z.string().default('随笔'),
    featured: z.boolean().default(false)
  })
});

export const collections = { posts };
