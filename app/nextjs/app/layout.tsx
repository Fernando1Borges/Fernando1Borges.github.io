/* eslint-disable react/jsx-props-no-spreading */
import React from 'react';
import '@rainbow-me/rainbowkit/styles.css';
import Head from 'next/head';
import Provider from './provider';

import './global.css';
import './index.css';

export const dynamic = 'force-dynamic';

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <Head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link
          rel="preconnect"
          href="https://fonts.gstatic.com"
          crossOrigin=""
        />
        <link
          href="https://fonts.googleapis.com/css2?family=Source+Code+Pro&display=swap"
          rel="stylesheet"
        />
      </Head>
      <body>
        <Provider>{children}</Provider>
      </body>
    </html>
  );
}
